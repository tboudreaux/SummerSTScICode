from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[209.533167,26.204306],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_135807.96+261215.5/sdB_sdssj_135807.96+261215.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_135807.96+261215.5/sdB_sdssj_135807.96+261215.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
