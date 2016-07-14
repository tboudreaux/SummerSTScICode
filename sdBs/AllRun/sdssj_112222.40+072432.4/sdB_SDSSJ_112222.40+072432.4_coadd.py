from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[170.593333,7.409],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_112222.40+072432.4/sdB_SDSSJ_112222.40+072432.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_112222.40+072432.4/sdB_SDSSJ_112222.40+072432.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
