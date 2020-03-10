export default [
  {
    path: '/candidato/:email',
    name: 'DetalhamentoCandidato',
    component: () => import(/* webpackChunkName: "about" */ './detalhamento')
  }
]
