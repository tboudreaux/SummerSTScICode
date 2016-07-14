from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[143.98225,36.5585],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_093555.74+363330.6/sdB_sdssj_093555.74+363330.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_093555.74+363330.6/sdB_sdssj_093555.74+363330.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()