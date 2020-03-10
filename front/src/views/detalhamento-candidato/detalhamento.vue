<template>
  <div class="p-3">
    <div class="text-center mt-5" v-if="loading">
      <h2>Buscando informações do candidato <i class="fa fa-spin fa-spinner"></i></h2>
    </div>

    <template v-else>
      <modal-comentario @ok="handleModalOk"/>
      <h1>{{ pageTitle }}</h1>
      <hr>
      {{ candidato.email }}

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
                <li v-for="(comentario, i) in comentarios" :key="i">
                  <div>Fase {{ i + 1}}</div>
                  <p>{{ comentario || '--' }}</p>
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

const fases = [
  'fase-01',
  'fase-02',
  'fase-03',
  'fase-04',
  'fase-05'
]

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
      if (this.faseAtual === 'fase-01') return 'Análise do currículo'
      if (this.faseAtual === 'fase-02') return 'Entrevista técnica'
      if (this.faseAtual === 'fase-03') return 'Teste prático'
      if (this.faseAtual === 'fase-04') return 'Entrevista comportamental e code review'
      if (this.faseAtual === 'fase-05') return 'Proposta'

      return ''
    },
    comentarios () {
      return this.candidato.progress.map(can => can.feedback)
    }
  },
  created () {
    this.buscarDadosCandidato()
  },
  data () {
    return {
      loading: false,
      modalAcao: null,
      faseAtual: null,
      candidato: {}
    }
  },
  methods: {
    abrirModalComentario (acao) {
      this.modalAcao = acao
      this.$root.$emit('comentario::show')
    },

    handleModalOk (comentario) {
      // console.log(`enviar request para api com a ação de: ${this.modalAcao} e o comentario: ${comentario}`)

      if (this.modalAcao === 'aprovar') {
        this.$http
          .post('progress_detail/', {
            feedback: comentario,
            user: this.candidato.id,
            stage: fases[fases.indexOf(this.faseAtual) + 1].replace('-', '_').replace('_0', '_').toUpperCase()
          })
          .then(res => {
            this.$router.push({
              name: 'ListaCandidatos'
            })
          })
      }

      if (this.modalAcao === 'reprovar') {
        this.$http
          .patch(`candidatos/${this.candidato.id}/`, { macro_status: 'ELIMINADO' })
          .then(res => () => {
            this.$router.push({
              name: 'ListaCandidatos'
            })
          })
      }

      this.$root.$emit('comentario::hide')
    },

    buscarDadosCandidato () {
      this.loading = true

      this.$http.get(`candidatos/${this.$route.query.id}/`)
        .then(res => {
          let fase = res.data.progress[res.data.progress.length - 1].stage
          fase = fase.replace('_', '-')
          fase = fase.toLowerCase()
          fase = fase.replace('-', '-0')

          this.faseAtual = fase
          this.candidato = res.data
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
