//实例化vue对象
var one = new Vue({
	el:'#vue-app-one',
	data:{
		title:"app one 内容",
	},
	methods: {
		
	},
	computed: {
		greet:function(){
			return "Hello App One";
		}
	},
});

var two = new Vue({
	el:'#vue-app-two',
	data:{
		title:"app two 内容",
	},
	methods: {
		changeTitle:function(){
			one.title = "已经改名了！"
		}
	},
	computed: {
		greet:function(){
			return "Hello App Two";
		}
	},
});

// two.title = "App Two的title也发生变化了"
 