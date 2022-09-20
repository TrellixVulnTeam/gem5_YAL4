# Copyright (c) 2015 ARM Limited
# All rights reserved.
#
# The license below extends only to copyright in the software and shall
# not be construed as granting a license to any other intellectual
# property including but not limited to intellectual property relating
# to a hardware implementation of the functionality of the software
# licensed hereunder.  You may use the software subject to the license
# terms below provided that you ensure that this notice is replicated
# unmodified and in its entirety in all distributions of the software,
# modified or unmodified, in source code or in binary form.
#
# Copyright (c) 2005-2007 The Regents of The University of Michigan
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from m5.defines import buildEnv
from m5.SimObject import SimObject
from m5.params import *
from m5.proxy import *
from m5.objects.PciDevice import PciDevice
from m5.objects.Ethernet import EtherInt


class SimBricksPci(PciDevice):
    type = 'SimBricksPci'
    cxx_class = 'simbricks::pci::Device'
    cxx_header = "simbricks/pci.hh"

    listen = Param.Bool(False, "Open listening instead of connecting")
    uxsocket_path = Param.String("unix socket path")
    shm_path = Param.String('', "Shared memory path")
    sync = Param.Bool(False, "Synchronize over PCI")
    poll_interval = Param.Latency('100us', "poll interval size (unsync only)")
    sync_tx_interval = Param.Latency('500ns', "interval between syncs")
    link_latency = Param.Latency('500ns', "PCI latency")

    Status = 0x0290
    MaximumLatency = 0x00
    MinimumGrant = 0xff
    SubsystemID = 0x1008
    SubsystemVendorID = 0x8086

    # defaults to avoid gem5 erroring out
    VendorID = 0x0001
    DeviceID = 0x0001


class SimBricksEthernet(SimObject):
    type = 'SimBricksEthernet'
    cxx_class = 'simbricks::ethernet::Adapter'
    cxx_header = "simbricks/ethernet.hh"

    int0 = EtherInt("interface 0")

    listen = Param.Bool(False, "Open listening instead of connecting")
    uxsocket_path = Param.String("unix socket path")
    shm_path = Param.String("Shared memory path")
    sync = Param.Bool(False, "Synchronize over Ethernet")
    poll_interval = Param.Latency('100us', "poll interval size (unsync only)")
    sync_tx_interval = Param.Latency('500ns', "interval between syncs")
    link_latency = Param.Latency('500ns', "Ethernet latency")


class SimBricksMem(SimObject):
    type = 'SimBricksMem'
    cxx_class = 'simbricks::mem::Adapter'
    cxx_header = "simbricks/mem.hh"

    port = SlavePort("Port to access the memory from CPU/Caches")

    listen = Param.Bool(False, "Open listening instead of connecting")
    uxsocket_path = Param.String("unix socket path")
    shm_path = Param.String(' ', "Shared memory path")
    sync = Param.Bool(False, "Synchronize over Ethernet")
    poll_interval = Param.Latency('100us', "poll interval size (unsync only)")
    sync_tx_interval = Param.Latency('500ns', "interval between syncs")
    link_latency = Param.Latency('500ns', "Ethernet latency")

    static_as_id = Param.UInt64(0x0, "Static address space ID for requests")
    base_address = Param.Addr("Memory Base Address")
    size = Param.Addr("Memory Size")