using BW.Net.Toolkit;
using BW.Web.ContractData;
using BW.Web.ContractModel;
using BW_GIS.Api;
using BW_GIS.Api.Common;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using NPOI.HSSF.UserModel;
using NPOI.SS.UserModel;
using System;
using System.Data;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Web.Http;

using System.Data.OleDb;

namespace WBW_GIS.Api.Controllers
{
    public class MyTestController : ApiController
    {
        //BW.Web.ContractLogic.BLL.Con_ContractBLL bll = new BW.Web.ContractLogic.BLL.Con_ContractBLL();
        BW.Web.ContractLogic.BLL.MyTestBLL bll = new BW.Web.ContractLogic.BLL.MyTestBLL();
        //BW.Web.ContractLogic.BLL.m_StaffBLL m_StaffBLL = new BW.Web.ContractLogic.BLL.m_StaffBLL();
        public readonly BW.Web.Contract_Sys.BLL.SysInfoBLL sys = new BW.Web.Contract_Sys.BLL.SysInfoBLL();
        CommonService service = new CommonService();
        string ip = CommonHepler.GetClientIPv4Address();

        #region 查询和列出
        [HttpOptions, HttpGet, TokenFilter(Islogin = true)]
        public Result List(string page = "", string rows = "", string sort = "", string order = "", string Title = "", string Time = "")
        {
            int intpage;
            if (!int.TryParse(page, out intpage))
            {
                return new Result("-1", "page格式不正确");
            }
            int introws;
            if (!int.TryParse(rows, out introws))
            {
                return new Result("-1", "rows格式不正确");
            }

            #region 验证输入值是否正确

            DateTime dateTime;
            string strSQL = @"select * from MyTest where 1=1 ";

            if (!string.IsNullOrEmpty(Title))
            {
                strSQL += "AND Title Like'%" + Title + "%'";
            }
            if (!string.IsNullOrEmpty(Time))
            {
                if (!DateTime.TryParse(Time, out dateTime))
                {
                    return new Result("-1", "Time格式不正确");
                }
                strSQL += "AND Time ='" + dateTime + "'";
            }
            #endregion
            //获得列表记录总数
            BW.Web.ContractLogic.BLL.Con_ContractBLL bll = new BW.Web.ContractLogic.BLL.Con_ContractBLL();
            DataTable dt = bll.Query(strSQL);
            //DataTable mydt1 = dt.SortPage(intpage + 1, introws, SortName, SortOrder);
            DataTable mydt1 = dt.SortPage(0, 20, sort, order);
            #region 返回值
            return new Result(new
            {
                total = dt.Rows.Count,
                rows = mydt1
            });
            #endregion
        }
        #endregion

        //#region Add
        //[HttpOptions, HttpPost, TokenFilter(Islogin = true)]
        //public Result Add()
        //{
        //    #region 验证输入值是否有效

        //    string Title = "";
        //    string Content = "";
        //    string Time = "";

        //    var body = HttpHelper.GetHttpContent();//获取body内容
        //    if (body.Trim() != "")
        //    {
        //        //解析body内容
        //        JObject jo;
        //        try
        //        {
        //            //解析body内容
        //            jo = (JObject)JsonConvert.DeserializeObject(body);
        //        }
        //        catch (Exception e)
        //        {
        //            return new Result("-1", "json格式不正确!");
        //        }
        //        Title = StringHelper.SqlFilter(jo["Title"]?.ToString());
        //        if (string.IsNullOrEmpty(Title))
        //        {
        //            return new Result("-1", "Title不能为空!");
        //        }
        //        Content = StringHelper.SqlFilter(jo["Content"]?.ToString());
        //        Content = Content.Replace("&lt", "<").Replace("&gt", ">");
        //        if (string.IsNullOrEmpty(Content))
        //        {
        //            return new Result("-1", "Content不能为空!");
        //        }
        //        Time = StringHelper.SqlFilter(jo["Time"]?.ToString());
        //        if (string.IsNullOrEmpty(Time))
        //        {
        //            return new Result("-1", "Time不能为空!");
        //        }
        //    }
        //    #endregion
        //    #region 验证输入值是否正确

        //    DateTime dateTime;
        //    if (!DateTime.TryParse(Time, out dateTime))
        //    {
        //        return new Result("-1", "Time格式不正确");
        //    }
        //    #endregion
        //    #region 获取返回值
        //    var model = new BW.Web.ContractLogic.Model.MyTest
        //    {
        //        Title = Title,
        //        Content = Content,
        //        Time = dateTime
        //    };
        //    var isChange = bll.Add(model);
        //    if (isChange <= 0)
        //    {
        //        return new Result("-1", "失败");
        //    }
        //    string remark = "新增测试" + Title;
        //    sys.Add(ControllerContext.Request.Properties["UserName"].ToString(), remark, ip);
        //    #endregion
        //    #region 返回值
        //    return new Result("0", "成功");
        //    #endregion
        //}
        //#endregion
        #region 新增/修改 -- 保存
        [HttpOptions, HttpPost, TokenFilter(Islogin = true)]
        public Result Save(dynamic obj)
        {
            if (obj == null)
            {
                return new Result("-1", "json格式不正确!");
            }
            int id = 0;
            bool result = false;
            if (obj.EF_MyTestInfo.ID == "0")   //新增 
            {
                MyTest myTest = Newtonsoft.Json.JsonConvert.DeserializeObject<MyTest>(Convert.ToString(obj.EF_MyTestInfo));
                result = service.Insert<MyTest>(myTest);
                if (!result) { return new Result("-1", "保存失败"); }

                id = myTest.Id;

            }
            else //修改
            {
                int Id = Convert.ToInt32(obj.EF_MyTestInfo.ID);
                var myTest = service.FindEntity<MyTest>(m => m.Id == Id);
                if (myTest == null) { return new Result("-1", "测试不存在"); }
                var check = service.GetList<MyTest>(m => m.Id == Id);
                myTest.Title = obj.EF_MyTestInfo.Title;
                myTest.Content = obj.EF_MyTestInfo.Content;
                myTest.Time = obj.EF_MyTestInfo.Time;
                result = service.Update<MyTest>(myTest);
                if (!result) { return new Result("-1", "保存失败"); }
                id = myTest.Id;
            }
            return new Result("0", id.ToString());
        }
        #endregion

        #region Delete
        [HttpOptions, HttpPost, TokenFilter(Islogin = true)]
        public Result Delete(int Id)
        {
            var result = service.DeleteBy<MyTest>(m => m.Id == Id);
            if (result == false)
            {
                return new Result("-1", "失败");
            }
            #region 返回值
            return new Result("0", "成功");
            #endregion
        }
        #endregion

        #region Info
        [HttpOptions, HttpGet, TokenFilter(Islogin = true)]
        public Result Info(string id)
        {
            int intId;
            if (!int.TryParse(id, out intId))
            {
                return new Result("-1", "Id格式不正确");
            }
            #region 获取返回值
            var MyTest = service.FindEntity<MyTest>(m => m.Id == intId);
            if (MyTest == null)
            {
                return new Result("-1", "数据不存在");
            }
            #endregion
            #region 返回值
            return new Result(MyTest);
            #endregion
        }
        #endregion


        /// <summary>
        /// 查询对应下拉框
        /// </summary>
        /// <returns></returns>
        [HttpOptions, HttpPost, TokenFilter(Islogin = true)]
        public Result Search()
        {
            string Field = "";
            var body = HttpHelper.GetHttpContent();//获取body内容
            JObject jo;
            jo = (JObject)JsonConvert.DeserializeObject(body);
            Field = StringHelper.SqlFilter(jo["Field"]?.ToString());
            if (Field == "")
            {
                return new Result("-1", "参数不能为空");
            }
            string strSQL = @"select Id from MyTest where 1=1 ";
            //获得列表记录总数
            BW.Web.ContractLogic.BLL.Con_ContractBLL bll = new BW.Web.ContractLogic.BLL.Con_ContractBLL();
            DataTable dt = bll.Query(strSQL);
            return new Result(dt);
        }

        #region 文件列表及上传

        /// <summary>
        /// 文件列表
        /// </summary>
        /// <returns></returns>
        [HttpOptions, HttpGet, TokenFilter(Islogin = true)]
        public Result FileList(string etid = "", string fileclass = "")
        {
            //if (string.IsNullOrEmpty(etid)) { return new Result("-1", "格式不正确"); }
            //if (string.IsNullOrEmpty(fileclass)) { return new Result("-1", "格式不正确"); }

            BW.Web.ContractLogic.BLL.Con_ContractBLL bll = new BW.Web.ContractLogic.BLL.Con_ContractBLL();

            DataTable dt = bll.Query(string.Format(@"select ID,FileUrl,RealName,CONVERT(nvarchar(10),CreateDT,120)CreateDT,(select Name from m_Staff where Id=CreateUserID)CreateUserID from dbo.FileCenter"));// where ID in (select FiledID from dbo.ET_TaskFiled where ETID={0} and ETClass={1})", etid, fileclass));

            return new Result(dt);
        }
        #endregion
        /// <summary>
        /// 上传文件
        /// </summary>
        /// <returns></returns>
        [HttpOptions, HttpPost, TokenFilter(Islogin = true)]
        public Result UpLoadFile()
        {
            System.Web.HttpRequest request = System.Web.HttpContext.Current.Request;
            // string taskID = request["ETID"].ToString().Trim();
            //int ETClass = Convert.ToInt32(request["ETClass"].ToString().Trim());
            // int tid = int.Parse(taskID);
            //var task = service.FindEntity<MyTest>(m => m.Id == tid);
            //if (task == null) return new Result("-1", "任务为空");

            System.Web.HttpFileCollection fileCollection = request.Files;
            if (fileCollection.Count < 1) return new Result("-1", "上传失败,文件为空");
            var fileinfo = UploadHelper.UploadFile(fileCollection[0]);
            if (fileinfo.IsSuccess == false) return new Result("-1", "上传失败");

            FileCenter newfile = new FileCenter();
            newfile.CreateDT = DateTime.Now;
            newfile.EndUserID = 0;
            newfile.RealName = fileinfo.OldFileName;
            newfile.FileName = fileinfo.NewFileName;
            newfile.FileUrl = fileinfo.FilePath;
            newfile.FileSize = fileCollection[0].ContentLength / 1000;
            newfile.CreateUserID = service.GetPersonID(ControllerContext.Request.Properties["WorkNo"].ToString());//请求人ID
            if (service.Insert<FileCenter>(newfile))
            {
                //ET_TaskFiled ET_TaskFiled = new ET_TaskFiled();
                //ET_TaskFiled.ETID = tid;
                //ET_TaskFiled.ETClass = ETClass;
                //ET_TaskFiled.FiledID = newfile.ID;
                //if (service.Insert<ET_TaskFiled>(ET_TaskFiled))
                //{
                return new Result("0", newfile.ID.ToString());
                //}
            }
            return new Result("-1", "上传失败");
        }




        #region Export
        /// <summary>
        /// 导出Excel表格
        /// </summary>
        /// <param name="body"></param>
        /// <returns></returns>
        [HttpGet]
        public HttpResponseMessage Export(string body)
        {
            #region 验证输入值是否有效
            string page = "";
            string size = "";
            string sort = "";
            string order = "";
            if (body.Trim() != "")
            {
                //解析body内容
                JObject jo;
                try
                {
                    //解析body内容
                    jo = (JObject)JsonConvert.DeserializeObject(body);
                }
                catch (Exception e)
                {
                    return new Result("-1", "json格式不正确!");
                }
                page = StringHelper.SqlFilter(jo["page"]?.ToString());
                if (string.IsNullOrEmpty(page))
                {
                    return new Result("-1", "page不能为空!");
                }
                size = StringHelper.SqlFilter(jo["rows"]?.ToString());
                if (string.IsNullOrEmpty(size))
                {
                    return new Result("-1", "size不能为空!");
                }
                sort = StringHelper.SqlFilter(jo["sort"]?.ToString());
                if (string.IsNullOrEmpty(sort))
                {
                    return new Result("-1", "sort不能为空!");
                }
                order = StringHelper.SqlFilter(jo["order"]?.ToString());
                if (string.IsNullOrEmpty(order))
                {
                    return new Result("-1", "order不能为空!");
                }
                //ContractNo = StringHelper.SqlFilter(jo["ContractNo"]?.ToString());

            }
            #endregion
            #region 验证输入值是否正确
            int intpage = 0;
            int intsize = 10;
            if (!int.TryParse(page, out intpage))
            {
                return new Result("-1", "page格式不正确");
            }
            if (intpage < 0)
            {
                return new Result("-1", "page不能小于0");
            }
            if (!int.TryParse(size, out intsize))
            {
                return new Result("-1", "size格式不正确");
            }

            #endregion
            #region 获取返回值
            DataTable dt = null;
            DataTable mydt1 = new DataTable();
            string strSQL = @"select * from MyTest where 1=1 ";
            //获得列表记录总数
            BW.Web.ContractLogic.BLL.Con_ContractBLL bll = new BW.Web.ContractLogic.BLL.Con_ContractBLL();
            dt = bll.Query(strSQL);
            mydt1 = dt.SortPage(intpage, intsize, sort, order);
            #endregion

            #region 设置显示列名,显示顺序


            HSSFWorkbook hssfworkbook = new HSSFWorkbook();

            ISheet sheet1 = hssfworkbook.CreateSheet("我的测试" + DateTime.Now.ToString("yyyyMMddHHmmss"));
            IRow rowHeader = sheet1.CreateRow(0);
            rowHeader.CreateCell(0).SetCellValue("序号");
            rowHeader.CreateCell(1).SetCellValue("标题");
            rowHeader.CreateCell(2).SetCellValue("内容");
            rowHeader.CreateCell(3).SetCellValue("日期");

            //生成excel内容
            for (int i = 0; i < dt.Rows.Count; i++)
            {
                NPOI.SS.UserModel.IRow rowtemp = sheet1.CreateRow(i + 1);
                rowtemp.CreateCell(0).SetCellValue(dt.Rows[i]["ID"].ToString());
                rowtemp.CreateCell(1).SetCellValue(dt.Rows[i]["Title"].ToString());
                rowtemp.CreateCell(2).SetCellValue(dt.Rows[i]["Content"].ToString());
                rowtemp.CreateCell(3).SetCellValue(dt.Rows[i]["Time"].ToString());
            }
            for (int i = 0; i < 10; i++)
                sheet1.AutoSizeColumn(i);

            MemoryStream file = new MemoryStream();
            hssfworkbook.Write(file);
            file.Seek(0, SeekOrigin.Begin);
            HttpResponseMessage result = new HttpResponseMessage(HttpStatusCode.OK);
            result.Content = new StreamContent(file);
            result.Content.Headers.ContentType = new MediaTypeHeaderValue("application/vnd.ms-excel");
            result.Content.Headers.ContentDisposition = new ContentDispositionHeaderValue("attachment");
            result.Content.Headers.ContentDisposition.FileName = InputHelper.StrToUTF("我的测试" + DateTime.Now.ToString("yyyyMMddHHmmss") + ".xls");
            return result;
            #endregion
        }
        #endregion


        #region ExcelOPT
        /// <summary>
        /// 
        /// </summary>
        /// <param name="ExcelFile"></param>
        /// <returns></returns>
        [HttpGet]
        public Result ExcelOPT(string ExcelFile)
        {
            string strSQL = @"select Id from MyTest where 1=1 ";
            //获得列表记录总数
            BW.Web.ContractLogic.BLL.Con_ContractBLL bll = new BW.Web.ContractLogic.BLL.Con_ContractBLL();
            DataTable dt = bll.Query(strSQL);


            string filename = @"D:\File\201802\b89b8f03-8545-45b0-abc8-63ce261697a3.xls";
            GetInfo(filename);
            return new Result(dt);

        }
        #endregion

        /// <summary>
        /// 
        /// </summary>
        /// <param name="ExcelFilePath"></param>
        /// <returns></returns>
        public Result GetInfo(string ExcelFilePath)
        {

            string fileSuffix = System.IO.Path.GetExtension(ExcelFilePath);

            if (string.IsNullOrEmpty(fileSuffix))

                return null;

            using (DataSet ds = new DataSet())

            {

                //判断Excel文件是2003版本还是2007版本

                string connString = "";

                if (fileSuffix == ".xls")
                {
                    connString = "Provider=Microsoft.Jet.OLEDB.4.0;" + "Data Source=" + ExcelFilePath + ";" + ";Extended Properties=\"Excel 8.0;HDR=YES;IMEX=1\"";

                }
                else
                {
                    connString = "Provider=Microsoft.ACE.OLEDB.12.0;" + "Data Source=" + ExcelFilePath + ";" + ";Extended Properties=\"Excel 12.0;HDR=YES;IMEX=1\"";

                    //读取文件

                    string sql_select = " SELECT * FROM [Sheet1$]";

                    using (OleDbConnection conn = new OleDbConnection(connString))

                    using (OleDbDataAdapter cmd = new OleDbDataAdapter(sql_select, conn))

                    {

                        conn.Open();

                        cmd.Fill(ds);

                    }

                    if (ds == null || ds.Tables.Count <= 0) return null;

                    //return ds;
                    return new Result(ds);

                }

            }
            return new Result("F");

        }
    }
}