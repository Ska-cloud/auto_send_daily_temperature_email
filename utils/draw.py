import datetime

from matplotlib import pyplot as plt

from utils.picture2base64 import convert_base64


class Draw:
    def __init__(self, data: list):
        self.data = data

        plt.rcParams["font.sans-serif"] = ["SimHei"]
        plt.title('近5天温度走势')
        plt.xlabel('日期')
        plt.ylabel('温度')
        self.high_temp = [a['high'] for a in data]
        self.date = [a['date'] for a in data]
        self.low_temp = [a['low'] for a in data]

    def draw_temperature(self) -> str:
        # 绘制最低温度
        plt.plot(self.date, self.low_temp, label='最高温度')
        # 绘制最高温度
        plt.plot(self.date, self.high_temp, label='最低温度')

        # 文字标注
        for i in range(5):
            plt.text(x=self.date[i],
                     y=self.low_temp[i],
                     s=f"{self.low_temp[i]}°")
            plt.text(x=self.date[i],
                     y=self.high_temp[i],
                     s=f"{self.high_temp[i]}°")

        plt.legend()

        save_file_path = f"./temperature_picture/{datetime.datetime.now().strftime('%Y-%m-%d')}.png"
        plt.savefig(save_file_path)
        base64_code = convert_base64(save_file_path)
        # plt.show()

        return base64_code


if __name__ == '__main__':
    ...
