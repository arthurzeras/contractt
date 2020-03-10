<template>
  <div class="p-3">
    <h1 class="text-capitalize">{{ faseAtual | fase }}</h1>
    <table class="table">
      <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Candidato</th>
      </tr>
      </thead>
      <tbody>
      <tr
        v-for="(candidato, index) in candidatos"
        :key="candidato.email"
      >
        <th scope="row">{{ index }}</th>
        <th>
          <router-link :to="{name: 'DetalhamentoCandidato', params: {email: candidato.email}, query: { fase: faseAtual }}">
            {{ candidato.email }}
          </router-link>
        </th>
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
    }
  },
  data () {
    return {
      candidatos: [
        {
          email: 'candidato1@email.com'
        },
        {
          email: 'candidato2@email.com'
        }
      ]
    }
  },
  filters: {
    fase (text) {
      return text.split('-').join(' ')
    }
  }
}
</script>

<style scoped>

</style>
