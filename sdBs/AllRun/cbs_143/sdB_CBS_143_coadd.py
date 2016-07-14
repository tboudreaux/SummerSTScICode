from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[174.24925,35.153439],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_CBS_143/sdB_CBS_143_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_CBS_143/sdB_CBS_143_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
