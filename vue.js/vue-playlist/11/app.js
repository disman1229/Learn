Vue.component('greeting',{
	template:`
	<p>
		{{name}}:欢迎来到我的博客！
		<button v-on:click="changeName">改名</button>
	</p>`,
	data:function(){
		return{
			name:"Disman",
		}
	},
	methods:{
		changeName:function(){
			this.name = "Disman1"
		}
	}
})
new	Vue({
	el:'#vue-app-one',
});
new	Vue({
	el:'#vue-app-two',
});
 