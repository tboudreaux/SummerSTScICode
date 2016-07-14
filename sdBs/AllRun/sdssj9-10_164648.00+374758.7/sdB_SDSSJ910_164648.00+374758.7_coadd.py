from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[251.7,37.799639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_164648.00+374758.7/sdB_SDSSJ910_164648.00+374758.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_164648.00+374758.7/sdB_SDSSJ910_164648.00+374758.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
