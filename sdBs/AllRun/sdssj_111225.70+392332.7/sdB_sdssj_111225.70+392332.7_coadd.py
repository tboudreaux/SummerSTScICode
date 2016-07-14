from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[168.107083,39.392417],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_111225.70+392332.7/sdB_sdssj_111225.70+392332.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_111225.70+392332.7/sdB_sdssj_111225.70+392332.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
