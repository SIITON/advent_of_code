using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace day_16
{
    public class PacketDecoder
    {
        public string ParseToBinary(string hexstring)
        {
            var binary = String.Join(String.Empty,
                hexstring.Select(c =>
                    Convert.ToString(Convert.ToInt32(c.ToString(), 16), 2).PadLeft(4, '0')
                    )
                );
            return binary;
        }
    }
}
