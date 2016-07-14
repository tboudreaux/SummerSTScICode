from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[255.480833,26.067556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_170155.40+260403.2/sdB_sdssj_170155.40+260403.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_170155.40+260403.2/sdB_sdssj_170155.40+260403.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
