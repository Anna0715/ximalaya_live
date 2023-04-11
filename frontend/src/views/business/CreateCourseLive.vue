<template>
  <div>
    <a-form :label-col="{ span: 3 }" :wrapper-col="{ span: 16 }" :form="form" @submit="onSubmit">
      <a-form-item :label="$t('createCourseLive.uid')">
        <a-input
          type="text"
          :placeholder="$t('createCourseLive.uid.placeholder')"
          v-decorator="[
            `uids`,
            {
              rules: [
                {
                  required: true,
                  message: '请输入uid',
                },
              ],
            },
          ]" />
      </a-form-item>

      <a-form-item :label="$t('createCourseLive.dropdown.label')">
        <a-select ref="select" v-model:value="dropdownValue" style="width: 120px" @change="handleDropdownChange">
          <a-select-option value="pay">{{ $t('createCourseLive.dropdown.pay.type') }}</a-select-option>
          <a-select-option value="formal">{{ $t('createCourseLive.dropdown.formal.type') }}</a-select-option>
          <a-select-option value="test">{{ $t('createCourseLive.dropdown.test.type') }}</a-select-option>
        </a-select>
      </a-form-item>

      <a-form-item :label="$t('createCourseLive.range.time')">
        <a-range-picker v-model:value="rangeTime" format="YYYY-MM-DD HH:mm:ss" @change="rangeTimeChange" />
      </a-form-item>

      <a-row>
        <a-col :span="1">
        </a-col>
        <a-col :span="6">
          <a-form-item :label="$t('createCourseLive.ticket.price')" :label-col="{ span: 8 }">
            <a-input-number
              v-model:value="price"
              :min="0"
              :formatter="value => `$ ${value}`.replace(/\B(?=(\d{3})+(?!\d))/g, ',')"
              :parser="value => value.replace(/\$\s?|(,*)/g, '')" />
          </a-form-item>
        </a-col>
        <a-col :span="6">
          <a-form-item :label="$t('createCourseLive.stock')" :label-col="{ span: 8 }">
            <a-input-number v-model:value="stock" :min="0" />
          </a-form-item>
        </a-col>
        <a-col :span="6">
          <a-form-item :label="$t('createCourseLive.ticket.sharing')" :label-col="{ span: 8 }">
            <a-input-number
              v-model:value="ticketSharing"
              :min="0"
              :max="70"
              :formatter="value => `${value}%`"
              :parser="value => value.replace('%', '')" />
          </a-form-item>
        </a-col>
      </a-row>

      <a-row>
        <a-col :span="1">
        </a-col>
        <a-col :span="6">
          <a-form-item :label="$t('createCourseLive.open.sale.check')" :label-col="{ span: 8 }">
            <a-switch :checked="openSale" @change="onOpenSaleChange" />
          </a-form-item>
        </a-col>
        <a-col :span="6">
          <a-form-item :label="$t('createCourseLive.open.play.back')" :label-col="{ span: 8 }">
            <a-tooltip>
              <template #title>{{ $t('createCourseLive.open.play.back.tip') }}</template>
              <a-switch :checked="showPlayback" :disabled="true" />
            </a-tooltip>
          </a-form-item>
        </a-col>
        <a-col :span="6">
          <a-form-item :label="$t('createCourseLive.open.send.gift')" :label-col="{ span: 8 }">
            <a-switch :checked="openSendGift" @change="onOpenSendGiftChange" />
          </a-form-item>
        </a-col>
      </a-row>

      <a-form-item :wrapper-col="{ span: 14, offset: 4 }">
        <a-button type="primary" html-type="submit">操作</a-button>
        <a-button style="margin-left: 10px" @click="resetForm">重置</a-button>
      </a-form-item>
    </a-form>

    <a-table :dataSource="dataSource" :columns="columns" bordered :loading="tableLoading">
      <template #title>{{ tableTitle }}</template>
    </a-table>

  </div>
</template>

<script>
import { createCourseLive } from '@/api/certification'
import { message } from 'ant-design-vue'
import moment from 'moment'

const timeFormat = 'YYYY-MM-DD HH:mm:ss'

export default {
  name: 'CreateCourseLive',
  data () {
    return {
      form: this.$form.createForm(this, { name: 'CreateCourseLive' }),
      uids: '',
      dropdownValue: 'pay',
      rangeTime: [moment().add(20, 'm').format(timeFormat), moment().add(50, 'm').format(timeFormat)],
      price: 10,
      stock: 1000,
      ticketSharing: 50,
      openSale: true,
      openSendGift: true,
      showPlayback: true,

      dataSource: [],
      tableTitle: '请求uid数量：0，成功数量：0',
      tableLoading: false,
      columns: [
        {
          title: 'uid',
          dataIndex: 'uid',
          key: 'uid',
          align: 'center'
        },
        {
          title: '返回信息',
          dataIndex: 'response',
          key: 'response',
          align: 'center'
        }
      ]
    }
  },
  methods: {
    handleDropdownChange (value) {
      this.dropdownValue = value
      if (value === 'test') {
        this.showPlayback = false
      } else {
        this.showPlayback = true
      }
    },
    rangeTimeChange (value) {
      this.rangeTime = [value?.[0]?.format(timeFormat), value?.[1]?.format(timeFormat)]
    },
    onOpenSaleChange () {
      this.openSale = !this.openSale
    },
    onOpenSendGiftChange () {
      this.openSendGift = !this.openSendGift
    },

    resetForm () {
      this.form.resetFields()
      this.dropdownValue = 'pay'
      this.rangeTime = [moment().add(20, 'm').format(timeFormat), moment().add(50, 'm').format(timeFormat)]
      this.price = 10
      this.stock = 1000
      this.ticketSharing = 50
      this.openSale = true
      this.openSendGift = true
      this.showPlayback = true
    },
    onSubmit (e) {
      e.preventDefault()
      const _this = this
      this.form.validateFields((error, values) => {
        console.log('error', error, values)
        if (!error) {
          _this.uids = values?.uids
          if (_this.uids) {
            _this.dataSource = []
            _this.tableLoading = true

            createCourseLive({
              uid: _this.uids,
              coursetype: _this.dropdownValueBeCourseType(_this.dropdownValue),
              openGoods: _this.openSale?.toString(),
              openGift: _this.openSendGift?.toString(),
              showPlayback: _this.showPlayback?.toString(),
              startAt: _this.rangeTime?.[0],
              endAt: _this.rangeTime?.[1],
              price: _this.price,
              quantity: _this.stock,
              clearRate: _this.ticketSharing
            }).then(res => {
              if (res.code === 200 && res?.data) {
                let successCount = 0
                res?.data?.map((item, index) => {
                  _this.dataSource.push({
                    key: (index + 1) + '',
                    uid: item?.uid,
                    response: item?.msg
                  })
                  if (item?.CeatecourseLive === 'success') {
                    successCount += 1
                  }
                })
                _this.tableTitle = `请求uid数量：${_this.dataSource.length}，成功数量：${successCount}`
              } else {
                message.error(res?.msg || '出错了，请@张柔')
                _this.tableTitle = res?.msg || '出错了，请@张柔'
              }
              _this.tableLoading = false
            }).catch(err => {
              message.error(err?.msg || '出错了，请@张柔')
              _this.tableTitle = err?.msg || '出错了，请@张柔'
              _this.tableLoading = false
            })
          }
        }
      })
    },
    dropdownValueBeCourseType (dropdownValue) {
      switch (dropdownValue) {
        case 'pay':
          return '付费'
        case 'formal':
          return '正式'
        case 'test':
          return '测试'
        default:
          return '付费'
      }
    }
  }
}
</script>

<style lang="less" scoped>
.item {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.item-uid-label {
  margin-right: 10px;
}
</style>
