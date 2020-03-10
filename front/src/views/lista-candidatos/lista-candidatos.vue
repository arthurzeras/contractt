<template>
  <div class="p-3">
    <h1>{{ pageTitle }}</h1>

    <div class="text-center mt-5" v-if="loading">
      <h2>Buscando candidatos <i class="fa fa-spin fa-spinner"></i></h2>
    </div>

    <table class="table" v-else>
      <thead>
      <tr>
        <th>#</th>
        <th>Candidato</th>
        <th v-if="faseAtual !== 'fase-01'">Status</th>
      </tr>
      </thead>
      <tbody>
      <tr
        v-for="(candidato, index) in candidatos"
        :key="candidato.email"
      >
        <td>{{ index }}</td>
        <td>
          <router-link :to="redirecionarRota(candidato)">
            {{ candidato.email }}
          </router-link>
        </td>
        <td v-if="faseAtual !== 'fase-01'">
          <span
            class="badge"
            :class="{
              'badge-danger' : candidato.status === 'pendente',
              'badge-success' : candidato.status === 'realizado',
            }"
          >{{ candidato.status }}</span>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Lista',

  computed: {
    faseAtual () {
      return this.$route.params.faseId
    },
    pageTitle () {
      if (this.$route.params.faseId === 'fase-01') return 'Análise do currículo'
      if (this.$route.params.faseId === 'fase-02') return 'Entrevista técnica'
      if (this.$route.params.faseId === 'fase-03') return 'Teste prático'
      if (this.$route.params.faseId === 'fase-04') return 'Entrevista comportamental e code review'
      if (this.$route.params.faseId === 'fase-05') return 'Proposta'

      return ''
    }
  },

  data () {
    return {
      loading: false,
      candidatos: []
    }
  },

  created () {
    this.buscarCandidatos()
  },

  methods: {
    buscarCandidatos (to) {
      this.loading = true

      // const fase = to ? to.params.faseId : this.$route.params.faseId

      this.$http.get('candidatos')
        .then(res => {
          this.candidatos = res.data
        })
        .finally(() => (this.loading = false))

      // console.log(`Buscando candidatos da ${fase}`)

      // setTimeout(() => {
      //   this.loading = false
      //   this.candidatos = [
      //     {
      //       email: 'candidato1@email.com',
      //       status: 'pendente'
      //     },
      //     {
      //       email: 'candidato2@email.com',
      //       status: 'realizado'
      //     }
      //   ]
      // }, 800)
    },

    redirecionarRota (candidato) {
      return {
        name: 'DetalhamentoCandidato',
        params: { email: candidato.email },
        query: { id: candidato.id }
      }
    }
  },

  beforeRouteUpdate (to, from, next) {
    this.buscarCandidatos(to)

    next()
  }
}
</script>

<style scoped>

</style>
