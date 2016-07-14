from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[194.924458,0.658],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_125941.87-003928.8/sdB_SDSSJ_125941.87-003928.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_125941.87-003928.8/sdB_SDSSJ_125941.87-003928.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
