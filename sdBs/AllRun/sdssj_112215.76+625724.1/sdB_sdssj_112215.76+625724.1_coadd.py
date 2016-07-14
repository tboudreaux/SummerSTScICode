from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[170.565667,62.956694],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_112215.76+625724.1/sdB_sdssj_112215.76+625724.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_112215.76+625724.1/sdB_sdssj_112215.76+625724.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
