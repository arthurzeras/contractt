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
      'Fase 01',
      'Primeira entrevista técnica',
      'Teste prático',
      'Fase 04',
      'Fase 05'
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
