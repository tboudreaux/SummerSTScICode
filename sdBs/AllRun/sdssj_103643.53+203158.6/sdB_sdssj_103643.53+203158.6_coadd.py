from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[159.181375,20.532944],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_103643.53+203158.6/sdB_sdssj_103643.53+203158.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_103643.53+203158.6/sdB_sdssj_103643.53+203158.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
