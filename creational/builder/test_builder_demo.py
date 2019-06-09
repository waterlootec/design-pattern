"""
Test stub to display usage of Builder design pattern.

Each House will be built based on builder provided.

Copyright (c) 2019, Waterlootec, Canada. All rights reserved.

Author: GAN MOHIM.
"""

from creational.builder.house_builder.duplex_builder import DuplexBuilder
from creational.builder.house_builder.cottage_builder import CottageBuilder
from creational.builder.developer import Developer


duplex = DuplexBuilder()
real_estate_dev = Developer(duplex)
house = real_estate_dev.build_house()
house.show_house()

cottage = CottageBuilder()
real_estate_dev = Developer(cottage)
house = real_estate_dev.build_house()
house.show_house()



