using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace day_08
{
    public class SignalDeterminator
    {
        public List<string> Input { get; set; }

        public int Decode(Func<int, bool> func)
        {
            var count = 0;
            foreach (var sequence in Input)
            {
                var signalPattern = sequence.Split("|")[1].Split(" ").ToList();
                foreach (var signal in signalPattern)
                {
                    if (func(signal.Length))
                    {
                        count++;
                    }
                }
            }

            return count;
        }
    }
}
