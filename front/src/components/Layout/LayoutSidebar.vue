<template>
  <nav class="layout-navbar">
    <ul class="nav flex-column">
      <li class="nav-item" v-for="(fase, index) in fases" :key="index">
        <router-link class="nav-link" :to="montarRota(index)">
          {{ fase }}
        </router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  data: () => ({
    fases: [
      'Análise do currículo',
      'Entrevista técnica',
      'Teste prático',
      'Entr. RH/Code Review',
      'Proposta'
    ]
  }),

  methods: {
    montarRota (fase) {
      return {
        name: 'ListaCandidatos',
        params: {
          faseId: `fase-0${fase}`
        }
      }
    }
  }
}
</script>

<style lang="scss">
  .layout-navbar {
    .nav-item {
      transition: .4s;
      border-bottom: 1px solid #ddd;

      &:hover {
        background-color: var(--light);
      }
    }
  }
</style>
