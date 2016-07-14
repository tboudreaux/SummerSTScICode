from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[158.076667,10.2905],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_103218.40+101725.8/sdB_SDSSJ_103218.40+101725.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_103218.40+101725.8/sdB_SDSSJ_103218.40+101725.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
