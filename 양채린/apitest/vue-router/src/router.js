import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

const About = () => {
  return import(/* webpackChunkName: "about" */ './views/About.vue')
}

// const About = () => {
//   return import(/* webpackChunkName: "about" */ './views/About.vue')
// }


export default new Router({ // 새로운 라우터를 만들어서 이 객체를 내보냄
  mode: 'history', // hash mode vs history mode
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/', // 이 주소창이 불리면
      name: 'home', // 컴포넌트와 연결된 또 하나의 별칭..?
      component: Home // 이 컴포넌트를 뿌려준다. 
    },
    {
      path: '/about',
      name: 'about-name',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.

      // SSA 이기 때문에 한 페이지에서 컴포넌트만 바뀌는 방식이다.
      // 주소창에 어떤 값이 입력되면, 해당되는 값에 해당하는 컴포넌트를 라우터가 찾는다.
      // lazy-loaded: 모든 것들을 잡아놓고 부르는 것이 아니라, 필요할 때마다 부른다는 뜻이다.
      // 함수 형태로 선언 후 값을 입력하면 필요할 때만 부른다.
      // 속도 면에서 차이가 존재한다.
      component: About
    }
  ]
})
