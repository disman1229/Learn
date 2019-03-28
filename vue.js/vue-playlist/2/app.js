//实例化vue对象
new	Vue({
	el:'#vue-app',
	data:{
		age:30,
		x:0,
		y:0,
	},
	methods: {
		add:function(increase){
			this.age += increase;
		},
		subtract:function(decrease){
			this.age -= decrease;
		},
		updateXY:function(event){
			// console.log(event)
			this.x = event.offsetX;
			this.y = event.offsetY;	
		},
		stopMoving:function(){
			event.stopPropagation();
		},
		alert:function(){
			alert("Hello World!")
		},
	},
});
 