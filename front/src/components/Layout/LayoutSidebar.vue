<template>
  <nav class="layout-navbar">
    <ul class="nav flex-column">
      <li class="nav-item" v-for="index in 5" :key="index">
        <router-link class="nav-link" :to="montarRota(index)">
          Fase {{ index }}
        </router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  methods: {
    montarRota (fase) {
      return {
        name: 'candidatos',
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
