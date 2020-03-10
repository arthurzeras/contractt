export default [
  {
    path: '/busca/:query',
    name: 'BuscarCandidato',
    component: () => import(/* webpackChunkName: "buscar-candidato" */ './BuscarCandidato')
  }
]
