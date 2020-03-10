export default [
  {
    path: '/candidatos/:faseId',
    name: 'ListaCandidatos',
    component: () => import(/* webpackChunkName: "about" */ './lista-candidatos')
  }
]
