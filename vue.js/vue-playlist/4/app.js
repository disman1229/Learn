//实例化vue对象
new	Vue({
	el:'#vue-app',
	data:{
		name:"Hello",
		age:30,
	},
	methods: {
		logName:function(){
			// console.log("你正在输入名字！")
			// this.name = this.$refs.name.value;
		},
		logAge:function(){
			// console.log("你正在输入年龄！")
			// this.age = this.$refs.age.value;
		}
	},
});
 