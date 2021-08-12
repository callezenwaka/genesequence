var app = new Vue({
	el: '#app',
	data: {
		isGenerating: false,
		isProtein: false,
		isSortProtein: false,
		file: '',
		sequence_option: '',
		sequence_output: '',
		sequence: {
			sequence_strand: '',
			sequence_type: '',
			sequence_length: 0,
			sequence_label: '',
		}
	},
	computed: {
		isValid() {
			return this.sequence.sequence_strand !== '' && this.sequence.sequence_type !== ''
		},
	},
	methods: {
		sortProtein(val) {
			if (val) {
				this.isSortProtein = true;
				this.sequence_output.sort((a,b) => b.length - a.length);
			}
			else {
				this.isSortProtein = false;
				this.sequence_output.sort((a,b) => a.length - b.length);
			}
		},
		generateSequence: function () {
			this.sequence_option = 'information'
			let sequence_length = +this.sequence.sequence_length;
			eel.generate(sequence_length, this.sequence.sequence_type)((val) => {
				this.sequence.sequence_label = val[0][0]
				this.sequence.sequence_type = val[0][1]
				this.sequence.sequence_length = val[0][2]
				this.sequence.sequence_strand = val[0][3]
				this.sequence_output = val[1]
			})
		},
		setSequence: function () {
			this.sequence_option = 'information'
			eel.set_Sequence(this.sequence)((val) => {
				this.sequence_output = val 
			})
		},
		set_output: function () {
			if (this.sequence_option === 'proteins') this.isProtein = true;
			else this.isProtein = false;
			eel.set_output(this.sequence, this.sequence_option)((val) => {
				this.sequence_output = val 
			})
		},
		selectFile () {
			this.$refs.file.click();
		},
		handleFileUpload: function () {
			// https://stackoverflow.com/a/42316936
			this.file = this.$refs.file.files[0];
			let reader = new FileReader();
			reader.onloadend = () => {
				const allLines = reader.result.split(/\r\n|\n/);
				// Reading line by line
				allLines.forEach((line) => {
					if (line.includes('>')) this.sequence.sequence_label = line
					else this.sequence.sequence_strand += line
				});
				this.sequence.sequence_type = this.sequence.sequence_strand.includes('T')? 'DNA' : 'RNA';
				this.sequence_option = 'information'
				eel.set_Sequence(this.sequence)((val) => {
					this.sequence_output = val 
				})
			};
			reader.onerror = () => {
				reader.abort();
			};
			reader.readAsText(this.file);
		},
	}
});