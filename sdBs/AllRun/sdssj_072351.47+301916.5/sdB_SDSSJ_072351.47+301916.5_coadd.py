from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[110.964458,30.32125],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_072351.47+301916.5/sdB_SDSSJ_072351.47+301916.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_072351.47+301916.5/sdB_SDSSJ_072351.47+301916.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()