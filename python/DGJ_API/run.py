# coding:utf-8

import unittest

from test_unnitest import Test
import HTMLTestRunner


def Case_Run():
    # 2种用法：第一种suite.addTest()
    # suite.addTest(Case('test_case01'))
    # suite.addTest(Case('test_case02'))
    # APP
    suite = unittest.TestSuite()
    suite.addTest(Test('test_GetVersion'))
    suite.addTest(Test('test_GetStationAppAdverList'))
    suite.addTest(Test('test_SystemNotice'))
    suite.addTest(Test('test_GetAppVersionList'))
    suite.addTest(Test('test_UploadSuggest'))
    suite.addTest(Test('test_GetSystemMsgAndAnnounceList'))
    # User
    suite.addTest(Test('test_VerificationAvailable'))
    suite.addTest(Test('test_QueryUserInfo'))
    suite.addTest(Test('test_WalletTradeInfo'))
    suite.addTest(Test('test_ChangeOperatorAddress'))
    suite.addTest(Test('test_WalletTradeHistory'))
    suite.addTest(Test('test_WalletTradeMoney'))
    # BasicInfo
    suite.addTest(Test('test_GetExpressCompany'))
    suite.addTest(Test('test_GetProvinceList'))
    suite.addTest(Test('test_GetIconList'))
    # SendOrder
    suite.addTest(Test('test_Statistics'))
    suite.addTest(Test('test_SendOrderSearch'))
    suite.addTest(Test('test_QueryBlackList'))
    suite.addTest(Test('test_Arrive'))
    suite.addTest(Test('test_Status'))
    suite.addTest(Test('test_QueryExpressCompanyByExpressNo'))
    suite.addTest(Test('test_ExpressInNew'))
    suite.addTest(Test('test_ExpressInSmartShelf'))
    suite.addTest(Test('test_ExpressOutNew'))
    suite.addTest(Test('test_Baginformation'))
    suite.addTest(Test('test_GetNotSignedWaybill'))
    suite.addTest(Test('test_GetJdStationReport'))
    suite.addTest(Test('test_MsgResendList'))
    suite.addTest(Test('test_SearchSuffix'))
    suite.addTest(Test('test_StatisticsList'))
    suite.addTest(Test('test_StatisticsStatusList'))
    # PostOrder
    suite.addTest(Test('test_StatisticsOrder'))
    suite.addTest(Test('test_StationSearchOrder'))
    suite.addTest(Test('test_PostOrderUrl'))
    suite.addTest(Test('test_AddressBookList'))
    suite.addTest(Test('test_CalcOrderAmout'))
    suite.addTest(Test('test_AddOrderElectronic'))
    suite.addTest(Test('test_StationOrderDetail'))
    suite.addTest(Test('test_EditIosDetails'))
    suite.addTest(Test('test_ProduceExpressNo'))
    # Station
    suite.addTest(Test('test_GetSyncData'))
    suite.addTest(Test('test_SetAddress'))
    suite.addTest(Test('test_GetStationDetailByAccountId'))
    suite.addTest(Test('test_SetContact'))
    suite.addTest(Test('test_SetOpeningTime'))
    suite.addTest(Test('test_GetStationSendFeeList'))
    suite.addTest(Test('test_RemoveDispatchCompany'))
    suite.addTest(Test('test_GetStationExpressList'))
    suite.addTest(Test('test_RemoveExpreeCompany'))
    suite.addTest(Test('test_GetCustomerLables'))
    suite.addTest(Test('test_GetCustomerList'))
    suite.addTest(Test('test_EquipmentList'))
    suite.addTest(Test('test_AddPrintEquipment'))
    suite.addTest(Test('test_GetSMSSetList'))
    suite.addTest(Test('test_GetSMSSet'))
    suite.addTest(Test('test_SetStationNotify'))
    suite.addTest(Test('test_GetStationIsOpenPostMustWeigh'))
    # KernelShelfBox
    suite.addTest(Test('test_SelShelfBoxOpen'))
    suite.addTest(Test('test_AddKernelShelfBoxList'))
    suite.addTest(Test('test_SelKernelShelfBoxList'))
    suite.addTest(Test('test_DelKernelShelfBox'))
    # SmsTemplate
    suite.addTest(Test('test_GetSmsTemplateTag'))
    suite.addTest(Test('test_GetTemplate'))
    suite.addTest(Test('test_AddTemplate'))
    # VoiceTemplate
    suite.addTest(Test('test_GetTemplateList'))
    suite.addTest(Test('test_GetVoiceTemplateTag'))
    suite.addTest(Test('test_AddTemplate'))
    # V2 订单重构
    # suite.addTest(Test('test_V2_Statistics'))
    # suite.addTest(Test('test_V2_SendOrderSearch'))
    # suite.addTest(Test('test_V2_Arrive'))
    # suite.addTest(Test('test_V2_ExpressInNew'))
    # suite.addTest(Test('test_V2_ExpressOutNew'))
    # suite.addTest(Test('test_V2_ExpressInSmartShelf'))

    # # 输出结果：测试结果直接输出在控制台
    # unittest.TextTestRunner(verbosity=2).run(suite)

    # 输出结果：将测试结果以report.html形式生成
    st = open('C:/Windows/ServiceProfiles/LocalService/.jenkins/workspace/DGJ_API/report/report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=st, title='递管家接口自动化测试报告', description='测试者：Jenkins自动化部署').run(suite)
    st.close()
    if runner.failure_count != 0:
        print('接口可能有异常,触发邮件')
        i = 1
        print("123" + i)


if __name__ == '__main__':
    Case_Run()
