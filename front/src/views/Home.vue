<template>
  <div class="home">
    <h1>Bem vindo(a) ao</h1>
    <img src="../assets/images/contractt-min.png" class="mt-4" width="400">
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style lang="scss">
  .home {
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
    height: calc(100vh - 200px);
  }
</style>
