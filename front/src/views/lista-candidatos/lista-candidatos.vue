<template>
  <div class="p-3">
    <h1>{{ pageTitle }}</h1>
    <table class="table">
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
          <router-link :to="{name: 'DetalhamentoCandidato', params: {email: candidato.email}, query: { fase: faseAtual }}">
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
      candidatos: [
        {
          email: 'candidato1@email.com',
          status: 'pendente'
        },
        {
          email: 'candidato2@email.com',
          status: 'realizado'
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
