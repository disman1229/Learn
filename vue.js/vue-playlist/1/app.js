//实例化vue对象
new	Vue({
	el:'#vue-app',
	data:{
		name:"Disman",
		job:"Web开发",
		website:"http://www.baidu.com/",
		websiteTag:"<a href='https://www.baidu.com'>百度</a>"
	},
	methods:{
		greet:function(time){
			return 'Good ' + time + " " + this.name + "!";
		}
	}
});
 