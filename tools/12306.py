from urllib import request
import json
import ssl
from stations_dict import stations_dict
from stations_dict_res import stations_dict_res
from prettytable import PrettyTable

ssl._create_default_https_context = ssl._create_unverified_context


def get_json(url, train_date, from_station, to_station, purpose_codes='ADULT'):
    url = url + '?leftTicketDTO.train_date=' + train_date + '&leftTicketDTO.from_station=' + from_station + '&leftTicketDTO.to_station=' + to_station + '&purpose_codes=' + purpose_codes
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
    req.add_header('Cookie',
                   'BLPROV=; JSESSIONID=17F82C085BEAE9774B1D7D18363207AA; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=1473839370.50210.0000; fp_ver=4.5.1; RAIL_EXPIRATION=1505522206734; RAIL_DEVICEID=ngfa0xXXc43Aw-RdePQiYKNAXLxgF_0NC4u29FDPVr73XbEdk2jAZXdZmGwbMs5tmX28EVf3pqQWywtJRANyU-F1F4o1jEN2J8gI5mQVerkJAel9E5ACri_F-7hggwk7zmV0IkRNjiH5CA0RFxBPLTsBkmBvAJ9_; current_captcha_type=C; _jc_save_fromStation=%u90D1%u5DDE%2CZZF; _jc_save_toStation=%u5F00%u5C01%2CKFF; _jc_save_fromDate=2017-09-25; _jc_save_toDate=2017-09-25; _jc_save_wfdc_flag=wf')
    with request.urlopen(req) as f:
        return json.loads(f.read())


def list_ticket(train_date, from_station, to_station):
    json_result = get_json('https://kyfw.12306.cn/otn/leftTicket/queryX', train_date, stations_dict.get(from_station),
                           stations_dict.get(to_station))
    list_tickets = json_result['data']['result']
    pt = PrettyTable()
    pt._set_field_names('车次 始发站 终点站 出发站 到达站 出发时间 到达时间 历时 商务座 一等座 二等座 软卧 硬卧 软座 硬座 无座 备注'.split())
    for ticket in list_tickets:
        list_ticket_item = ticket.split('|')
        pt.add_row([list_ticket_item[3], stations_dict_res.get(list_ticket_item[4]),
                    stations_dict_res.get(list_ticket_item[5]),
                    stations_dict_res.get(list_ticket_item[6]), stations_dict_res.get(list_ticket_item[7]),
                    list_ticket_item[8], list_ticket_item[9], list_ticket_item[10], list_ticket_item[32],
                    list_ticket_item[31],
                    list_ticket_item[30], list_ticket_item[23], list_ticket_item[28], list_ticket_item[24],
                    list_ticket_item[29], list_ticket_item[26], list_ticket_item[11]])
    print(pt)


def main():
    list_ticket('2017-09-25', '郑州', '北京')


if __name__ == '__main__':
    main()
