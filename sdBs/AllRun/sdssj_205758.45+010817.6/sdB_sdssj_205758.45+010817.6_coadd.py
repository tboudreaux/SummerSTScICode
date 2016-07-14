from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[314.493542,1.138222],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_205758.45+010817.6/sdB_sdssj_205758.45+010817.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_205758.45+010817.6/sdB_sdssj_205758.45+010817.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
