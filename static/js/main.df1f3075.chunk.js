(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{10:function(e,t,n){e.exports=n(18)},15:function(e,t,n){},17:function(e,t,n){},18:function(e,t,n){"use strict";n.r(t);var a=n(0),r=n.n(a),s=n(5),c=n.n(s),o=(n(15),n(1)),i=n.n(o),u=n(3),l=n(2),h=n(6),m=n(7),p=n(9),f=n(8);function d(e,t,n){return new Promise(function(){var a=Object(l.a)(i.a.mark((function a(r,s){var c,o,u;return i.a.wrap((function(a){for(;;)switch(a.prev=a.next){case 0:return c=e.length?JSON.stringify({alreadyFeatures:e,params:t,answers:n}):JSON.stringify({}),a.prev=1,a.next=4,fetch("".concat("http://localhost:5000","/api/questions/"),{method:"POST",headers:{"content-type":"application/json"},body:c});case 4:return o=a.sent,a.next=7,o.json();case 7:u=a.sent,r(u),a.next=15;break;case 11:a.prev=11,a.t0=a.catch(1),console.log(a.t0),s("Error on get Question");case 15:case"end":return a.stop()}}),a,null,[[1,11]])})));return function(e,t){return a.apply(this,arguments)}}())}n(17);var v=function(e){var t=e.question,n=e.answersButtons,a=e.onButtonClick;return r.a.createElement("div",{className:"searchContainer"},r.a.createElement("img",{src:"/brain.png",alt:""}),r.a.createElement("h2",null,t),r.a.createElement("div",null,n.map((function(e){return r.a.createElement("button",{key:Math.random(),onClick:function(){return a(e.value)}},e.title)}))))},w=function(e){var t=e.characterMatch;return r.a.createElement("div",{className:"finishedContainer"},r.a.createElement("img",{src:t.image,alt:""}),r.a.createElement("h2",null,t.name))},g=function(e){Object(p.a)(n,e);var t=Object(f.a)(n);function n(){var e;Object(h.a)(this,n);for(var a=arguments.length,r=new Array(a),s=0;s<a;s++)r[s]=arguments[s];return(e=t.call.apply(t,[this].concat(r))).state={alreadyFeatures:[],params:[],answers:[],answersButtons:[],question:"",characterMatch:null,loading:!0,finished:!1},e.setQuestion=Object(l.a)(i.a.mark((function t(){var n,a,r,s,c,o,l,h,m;return i.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return e.setState({loading:!0}),t.prev=1,n=e.state,a=n.alreadyFeatures,r=n.params,t.next=5,d(a,r,e.state.answers);case 5:s=t.sent,c=s.answers,o=s.characterMatch,l=s.feature,h=s.param,m=s.question,e.setState({params:[].concat(Object(u.a)(e.state.params),[h]),alreadyFeatures:[].concat(Object(u.a)(e.state.alreadyFeatures),[l]),answersButtons:c,characterMatch:o,question:m,loading:!1}),t.next=19;break;case 14:t.prev=14,t.t0=t.catch(1),console.log(t.t0),e.setState({loading:!1}),alert("Error on get Question");case 19:case"end":return t.stop()}}),t,null,[[1,14]])}))),e.onButtonClick=function(){var t=Object(l.a)(i.a.mark((function t(n){return i.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,e.setState({answers:[].concat(Object(u.a)(e.state.answers),[n])});case 2:return t.next=4,e.setQuestion();case 4:12===e.state.answers.length&&e.setState({finished:!0});case 6:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),e}return Object(m.a)(n,[{key:"componentWillMount",value:function(){this.setQuestion()}},{key:"render",value:function(){var e=this.state,t=e.question,n=e.answersButtons,a=e.loading,s=e.finished,c=e.characterMatch;return r.a.createElement("div",{className:"app"},r.a.createElement("header",null,r.a.createElement("h1",null,"I WILL DISCOVER YOUR SUPERHERO!")),r.a.createElement("main",null,a&&!s?r.a.createElement("h2",null,"Carregando.."):null,a||s?null:r.a.createElement(v,{question:t,answersButtons:n,onButtonClick:this.onButtonClick}),s?r.a.createElement(w,{characterMatch:c}):null))}}]),n}(a.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));c.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(g,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[10,1,2]]]);
//# sourceMappingURL=main.df1f3075.chunk.js.map