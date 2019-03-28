//实例化vue对象
new	Vue({
	el:'#vue-app',
	data:{
		name:"Disman",
		job:"Web开发",
	},
	methods:{
		greet:function(time){
			return 'Good ' + time + " " + this.name + "!";
		}
	}
});
 