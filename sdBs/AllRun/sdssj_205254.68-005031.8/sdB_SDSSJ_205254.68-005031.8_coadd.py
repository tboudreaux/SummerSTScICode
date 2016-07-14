from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[313.227833,0.842167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_205254.68-005031.8/sdB_SDSSJ_205254.68-005031.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_205254.68-005031.8/sdB_SDSSJ_205254.68-005031.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
