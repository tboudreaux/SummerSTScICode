from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[120.312792,37.234472],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_080115.07+371404.1/sdB_sdssj_080115.07+371404.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_080115.07+371404.1/sdB_sdssj_080115.07+371404.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
