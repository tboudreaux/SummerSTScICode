from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[188.083708,26.153694],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_123220.09+260913.3/sdB_sdssj_123220.09+260913.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_123220.09+260913.3/sdB_sdssj_123220.09+260913.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
