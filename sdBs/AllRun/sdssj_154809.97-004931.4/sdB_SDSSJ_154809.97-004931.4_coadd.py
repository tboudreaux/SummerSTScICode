from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[237.041542,0.825389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_154809.97-004931.4/sdB_SDSSJ_154809.97-004931.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_154809.97-004931.4/sdB_SDSSJ_154809.97-004931.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
