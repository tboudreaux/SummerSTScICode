from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[127.803958,39.79175],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_083112.95+394730.3/sdB_sdssj_083112.95+394730.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_083112.95+394730.3/sdB_sdssj_083112.95+394730.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
