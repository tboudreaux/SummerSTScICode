from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[190.412042,-62.648608],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_cs_1238/sdB_cs_1238_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_cs_1238/sdB_cs_1238_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
