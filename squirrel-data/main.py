# Copyright 2021 Timmy Olsson
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# how many of each color fur is there ( Primary Fur Color )
#New csv with this data.

import pandas

data = pandas.read_csv("./squirrel_data.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Amount': [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

new_data = pandas.DataFrame(data_dict)

new_data.to_csv("./colors.csv")