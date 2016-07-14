from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[260.238292,-36.497778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SC_1717-364/sdB_SC_1717-364_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SC_1717-364/sdB_SC_1717-364_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
