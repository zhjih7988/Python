select a.ID, a.NO,a.ApplyPeople,a.Supplier,a.Money,a.ApplyDT, 
case b.AuditLevel
when 1 then '发起申请'
when 2 then '经理审核'
when 3 then '副总审核'
when 4 then '总经理审核'
when 5 then '等待付款'
when 6 then '完成付款'
end as AuditLevel
from Pay_Manage a
left join Pay_ManageRecord b on b.NO = a.NO