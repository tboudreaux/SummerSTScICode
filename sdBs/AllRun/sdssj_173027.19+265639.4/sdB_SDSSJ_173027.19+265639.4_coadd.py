from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[262.613292,26.944278],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_173027.19+265639.4/sdB_SDSSJ_173027.19+265639.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_173027.19+265639.4/sdB_SDSSJ_173027.19+265639.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
