<template>
  <div class="p-3">
    <div class="text-center mt-5" v-if="loading">
      <h2>Buscando informações do candidato <i class="fa fa-spin fa-spinner"></i></h2>
    </div>

    <template v-else>
      <modal-comentario @ok="handleModalOk"/>
      <h1>{{ pageTitle }}</h1>
      <hr>
      {{ candidato }}

      <div class="row">
        <div class="col-md-8" :class="{'col-md-12': faseAtual === 'fase-01'}">
          <component
            :is="componenteAtual"
            @finalizar="abrirModalComentario"
          />
        </div>
        <div class="col-md-4" v-if="faseAtual !== 'fase-01'">
          <div class="card mt-2 mb-2">
            <div class="card-header">Comentários</div>
            <div class="card-body">
              <ul>
                <li>
                  <div>Fase 1:</div>
                  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. At consequatur corporis, debitis est molestiae natus soluta. Alias autem consequuntur, doloribus eum excepturi minus molestias nobis non ratione sed tenetur voluptatem.</p>
                </li>
                <li>
                  <div>Fase 2:</div>
                  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Culpa delectus eaque ex explicabo, incidunt laudantium magni modi mollitia nostrum odit omnis, quos, repellendus sapiente similique sit sunt velit veritatis voluptates.</p>
                </li>
                <li>
                  <div>Fase 3:</div>
                  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur dolor ducimus eius, esse ipsam magni maiores, maxime neque, officia omnis ratione soluta tempore! Blanditiis earum iure obcaecati quibusdam reprehenderit ut?</p>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script>
import Fase01 from '../fase-01/fase-01'
import Fase02 from '../fase-02/fase-02'
import Fase03 from '../fase-03/fase-03'
import Fase04 from '../fase-04/fase-04'
import Fase05 from '../fase-05/fase-05'
import ModalComentario from '@/components/ModalComentario'

export default {
  name: 'Lista',
  components: {
    // eslint-disable-next-line vue/no-unused-components
    Fase01,
    Fase02,
    Fase03,
    Fase04,
    Fase05,
    ModalComentario
  },
  computed: {
    componenteAtual () {
      return new Map([
        ['fase-01', Fase01],
        ['fase-02', Fase02],
        ['fase-03', Fase03],
        ['fase-04', Fase04],
        ['fase-05', Fase05]
      ]).get(this.faseAtual)
    },
    pageTitle () {
      if (this.$route.query.fase === 'fase-01') return 'Análise do currículo'
      if (this.$route.query.fase === 'fase-02') return 'Entrevista técnica'
      if (this.$route.query.fase === 'fase-03') return 'Teste prático'
      if (this.$route.query.fase === 'fase-04') return 'Entrevista comportamental e code review'
      if (this.$route.query.fase === 'fase-05') return 'Proposta'

      return ''
    },
    candidato () {
      return this.$route.params.email
    }
  },
  created () {
    this.buscarDadosCandidato()
  },
  data () {
    return {
      loading: false,
      modalAcao: null,
      faseAtual: null
    }
  },
  methods: {
    abrirModalComentario (acao) {
      this.modalAcao = acao
      this.$root.$emit('comentario::show')
    },

    handleModalOk (comentario) {
      console.log(`enviar request para api com a ação de: ${this.modalAcao} e o comentario: ${comentario}`)
      this.$root.$emit('comentario::hide')
    },

    buscarDadosCandidato () {
      this.loading = true

      this.$http.get(`candidato/${this.$route.query.id}`)
        .then(res => {
          console.log(res.data)
        })
        .finally(() => (this.loading = false))

      // setTimeout(() => {
      //   this.faseAtual = this.$route.query.fase
      //   this.loading = false
      // }, 800)
    }
  }
}
</script>

<style scoped>

</style>
